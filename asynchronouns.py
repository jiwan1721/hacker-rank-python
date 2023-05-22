async def get_chat_id(name):
    await asyncio.sleep(3)
    return f"helll {name}"

async def main():
    result = get_chat_id('jiwan')
    result1 = await result
    print("------",result1)

    await main()