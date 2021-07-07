from gino import Gino


db = Gino()

async def create_db():
    await ds.set_bind(POSTGREURI)