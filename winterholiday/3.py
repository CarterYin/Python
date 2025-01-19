import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional, List, Dict, Tuple
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor
import logging

# 设置日志配置
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class StockMetrics:
    """存储股票分析指标的数据类"""
    symbol: str
    mean_return: float
    volatility: float
    sharpe_ratio: float
    max_drawdown: float
    beta: float


class StockAnalyzer:
    """股票数据分析类"""

    def __init__(self, risk_free_rate: float = 0.02):
        self.risk_free_rate = risk_free_rate
        self._market_data: Optional[pd.DataFrame] = None
        self._stocks_data: Dict[str, pd.DataFrame] = {}

    # 在 fetch_data 方法中修改市场数据获取部分
    def fetch_data(self, symbols: List[str], start_date: str, end_date: str) -> None:
        """
        获取股票数据，使用多线程提高效率
        """

        def _fetch_single_stock(symbol: str) -> Tuple[str, Optional[pd.DataFrame]]:
            try:
                stock = yf.Ticker(symbol)
                data = stock.history(start=start_date, end=end_date)
                # 确保时区一致
                data.index = data.index.tz_localize(None)
                return symbol, data
            except Exception as e:
                logger.error(f"Error fetching data for {symbol}: {str(e)}")
                return symbol, None

        # 获取市场指数数据（以S&P500为例）
        try:
            self._market_data = yf.download('^GSPC', start=start_date, end=end_date)
            # 移除时区信息
            self._market_data.index = self._market_data.index.tz_localize(None)
        except Exception as e:
            logger.error(f"Error fetching market data: {str(e)}")
            raise

        # 使用线程池并行获取多个股票数据
        with ThreadPoolExecutor(max_workers=5) as executor:
            results = executor.map(lambda x: _fetch_single_stock(x), symbols)

        for symbol, data in results:
            if data is not None:
                self._stocks_data[symbol] = data

    def calculate_metrics(self, symbol: str) -> Optional[StockMetrics]:
        """计算单个股票的各项指标"""
        try:
            stock_data = self._stocks_data.get(symbol)
            if stock_data is None:
                return None

            # 计算日收益率
            stock_returns = stock_data['Close'].pct_change().dropna()
            market_returns = self._market_data['Close'].pct_change().dropna()

            # 确保数据对齐
            aligned_data = pd.concat([stock_returns, market_returns], axis=1).dropna()
            stock_returns = aligned_data.iloc[:, 0]
            market_returns = aligned_data.iloc[:, 1]

            # 计算年化收益率和波动率
            mean_return = stock_returns.mean() * 252  # 252个交易日
            volatility = stock_returns.std() * np.sqrt(252)

            # 计算夏普比率
            sharpe_ratio = (mean_return - self.risk_free_rate) / volatility

            # 计算最大回撤
            cumulative_returns = (1 + stock_returns).cumprod()
            rolling_max = cumulative_returns.expanding().max()
            drawdowns = cumulative_returns / rolling_max - 1
            max_drawdown = drawdowns.min()

            # 计算贝塔系数
            covariance = stock_returns.cov(market_returns)
            market_variance = market_returns.var()
            beta = covariance / market_variance

            return StockMetrics(
                symbol=symbol,
                mean_return=mean_return,
                volatility=volatility,
                sharpe_ratio=sharpe_ratio,
                max_drawdown=max_drawdown,
                beta=beta
            )

        except Exception as e:
            logger.error(f"Error calculating metrics for {symbol}: {str(e)}")
            return None

    def plot_performance_comparison(self, symbols: List[str]) -> None:
        """绘制股票表现对比图"""
        plt.figure(figsize=(15, 10))

        # 创建子图
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 12))

        # 绘制累积收益对比
        for symbol in symbols:
            if symbol in self._stocks_data:
                returns = self._stocks_data[symbol]['Close'].pct_change()
                cumulative_returns = (1 + returns).cumprod()
                ax1.plot(cumulative_returns.index, cumulative_returns, label=symbol)

        ax1.set_title('Cumulative Returns Comparison')
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Cumulative Return')
        ax1.legend()
        ax1.grid(True)

        # 绘制风险收益散点图
        metrics = []
        for symbol in symbols:
            metric = self.calculate_metrics(symbol)
            if metric:
                metrics.append(metric)

        if metrics:
            returns = [m.mean_return for m in metrics]
            vols = [m.volatility for m in metrics]
            ax2.scatter(vols, returns)

            # 添加标签
            for metric in metrics:
                ax2.annotate(
                    metric.symbol,
                    (metric.volatility, metric.mean_return),
                    xytext=(5, 5),
                    textcoords='offset points'
                )

        ax2.set_title('Risk-Return Profile')
        ax2.set_xlabel('Volatility (Risk)')
        ax2.set_ylabel('Expected Return')
        ax2.grid(True)

        plt.tight_layout()
        plt.show()

    def generate_report(self, symbols: List[str]) -> pd.DataFrame:
        """生成分析报告"""
        metrics_list = []
        for symbol in symbols:
            metrics = self.calculate_metrics(symbol)
            if metrics:
                metrics_list.append({
                    'Symbol': metrics.symbol,
                    'Annual Return': f"{metrics.mean_return:.2%}",
                    'Volatility': f"{metrics.volatility:.2%}",
                    'Sharpe Ratio': f"{metrics.sharpe_ratio:.2f}",
                    'Max Drawdown': f"{metrics.max_drawdown:.2%}",
                    'Beta': f"{metrics.beta:.2f}"
                })

        return pd.DataFrame(metrics_list)


def main():
    """主函数"""
    # 示例使用
    analyzer = StockAnalyzer()
    symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']

    try:
        # 获取过去一年的数据
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365)

        # 获取数据
        analyzer.fetch_data(symbols, start_date.strftime('%Y-%m-%d'),
                            end_date.strftime('%Y-%m-%d'))

        # 生成报告
        report = analyzer.generate_report(symbols)
        print("\nStock Analysis Report:")
        print(report)

        # 绘制图表
        analyzer.plot_performance_comparison(symbols)

    except Exception as e:
        logger.error(f"Analysis failed: {str(e)}")
        raise


if __name__ == "__main__":
    main()