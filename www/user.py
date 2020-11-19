import orms
from models import User
import asyncio

async def test(loop):
    await orms.create_pool(user='root', password='123456', db='awesome', loop=loop)

    u = User(name='Test', email='test@example.com', passwd='1234567', image='about:blank')
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))