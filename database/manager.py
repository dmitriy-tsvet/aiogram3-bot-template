from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import create_engine
import typing
from . import base


async def create_async_session(database: base.AsyncDatabase, *args, **kwargs):
    engine = create_async_engine(database, future=True, *args, **kwargs)
    Session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    return Session


def create_session(database: typing.Union[base.TransactionDatabase, base.FileDatabase], *args, **kwargs):
    engine = create_engine(url=str(database), future=True, *args, **kwargs)
    Session = sessionmaker(bind=engine)
    return Session


# async def select(session, query):
#     async with session.begin() as _session:
#         result = _session.execute(query)
#         return result.scalars()
#
#
# async def add(query, session):
#     async with session.begin() as _session:
#         result = _session.add(query)
#         return result.scalars()
#
#
# async def delete(query, session):
#     async with session.begin() as _session:
#         result = _session.add(query)

