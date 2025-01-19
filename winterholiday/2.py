from typing import List, Optional, Dict
from datetime import datetime, timedelta
from abc import ABC, abstractmethod
import json
from dataclasses import dataclass
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class Author:
    """作者信息数据类"""
    name: str
    birth_year: int
    nationality: str


class Book:
    """图书类，使用属性装饰器和私有属性示范"""

    def __init__(self, title: str, author: Author, isbn: str, total_copies: int):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._total_copies = total_copies
        self._available_copies = total_copies
        self._borrowed_by: Dict[str, datetime] = {}

    @property
    def title(self) -> str:
        return self._title

    @property
    def available_copies(self) -> int:
        return self._available_copies

    def borrow_book(self, user_id: str) -> bool:
        """借书方法，展示异常处理"""
        try:
            if self._available_copies > 0 and user_id not in self._borrowed_by:
                self._available_copies -= 1
                self._borrowed_by[user_id] = datetime.now()
                logger.info(f"Book '{self._title}' borrowed by user {user_id}")
                return True
            return False
        except Exception as e:
            logger.error(f"Error borrowing book: {str(e)}")
            raise


class LibraryUser:
    """图书馆用户类，展示类方法和实例方法"""
    _total_users = 0  # 类变量示例

    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name
        self.borrowed_books: List[str] = []  # ISBN列表
        LibraryUser._total_users += 1

    @classmethod
    def get_total_users(cls) -> int:
        """类方法示例"""
        return cls._total_users


class LibrarySystem:
    """图书馆系统类，展示单例模式"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._books: Dict[str, Book] = {}  # ISBN -> Book
        self._users: Dict[str, LibraryUser] = {}  # user_id -> User
        self._initialized = True

    def add_book(self, book: Book) -> None:
        """添加图书，展示类型注解"""
        self._books[book._isbn] = book

    def register_user(self, name: str) -> str:
        """注册新用户，展示ID生成"""
        user_id = f"USER{len(self._users) + 1:04d}"
        self._users[user_id] = LibraryUser(user_id, name)
        return user_id

    def borrow_book(self, user_id: str, isbn: str) -> bool:
        """借书流程，展示复杂业务逻辑处理"""
        if user_id not in self._users or isbn not in self._books:
            return False

        user = self._users[user_id]
        book = self._books[isbn]

        if len(user.borrowed_books) >= 3:  # 最多借3本书
            logger.warning(f"User {user_id} has reached maximum borrowing limit")
            return False

        if book.borrow_book(user_id):
            user.borrowed_books.append(isbn)
            return True
        return False


def main():
    """主函数，展示系统使用方式"""
    try:
        # 创建图书馆系统实例
        library = LibrarySystem()

        # 添加一些作者和图书
        author1 = Author("J.K. Rowling", 1965, "British")
        book1 = Book("Harry Potter", author1, "978-0-7475-3269-9", 5)
        library.add_book(book1)

        # 注册用户
        user_id = library.register_user("John Doe")

        # 借书
        if library.borrow_book(user_id, "978-0-7475-3269-9"):
            print(f"Successfully borrowed book for user {user_id}")
        else:
            print("Failed to borrow book")

    except Exception as e:
        logger.error(f"System error: {str(e)}")
        raise


if __name__ == "__main__":
    main()