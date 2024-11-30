import asyncio
import time
from fastapi import FastAPI

app = FastAPI()

# Global counters to track the number of requests for each endpoint
count_asyncdef_without_await = 0
count_asyncdef_with_await = 0
count_def_normal = 0


# Normal synchronous function
def normal_function(request_number):
    print(f"Normal function called for request number {request_number}")
    time.sleep(2)  # Blocking operation
    return f"Processed by normal_function for request {request_number}"

# Asynchronous function
async def async_function(request_number):
    print(f"Async function called for request number {request_number}")
    await asyncio.sleep(3)  # Non-blocking operation
    return f"Processed by async_function for request {request_number}"

@app.get("/asyncdef_without_await")
async def asyncdef_without_await():
    global count_asyncdef_without_await
    count_asyncdef_without_await += 1
    current_request = count_asyncdef_without_await
    print(f"Processing request number {current_request} for asyncdef_without_await")
    time.sleep(3)  # Blocking operation
    print(f"Function asyncdef_without_await completed for request number {current_request}")
    return {"message": f"Processed request number {current_request} for asyncdef_without_await"}


@app.get("/asyncdef_with_await")
async def asyncdef_with_await():
    global count_asyncdef_with_await
    count_asyncdef_with_await += 1
    current_request = count_asyncdef_with_await
    print(f"Processing request number {current_request} for asyncdef_with_await")
    

    # Call the normal function
    normal_function_result = normal_function(current_request)
    print(f"Normal function returned: {normal_function_result}")

    

    # Call the asynchronous function
    async_function_result = await async_function(current_request)
    print(f"Async function completed for request number {current_request}")



    return {
        "message": f"Processed request number {current_request} for asyncdef_with_await",
        "normal_function_result": normal_function_result,
        "async_function_result": async_function_result
    }



@app.get("/def_normal")
def def_normal():
    global count_def_normal
    count_def_normal += 1
    current_request = count_def_normal
    print(f"Processing request number {current_request} for def_normal")
    time.sleep(3)  # Blocking operation
    print(f"Function def_normal completed for request number {current_request}")
    return {"message": f"Processed request number {current_request} for def_normal"}
