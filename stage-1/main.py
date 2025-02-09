from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from fastapi.responses import JSONResponse
from model.numberResponse import NumberResponse
from service.numberService import is_armstrong, is_prime, is_perfect, get_digit_sum, get_number_properties, get_fun_fact, is_numeric, is_valid_number

app = FastAPI()


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust the origins as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/classify-number", response_model=NumberResponse)
async def classify_number(number):
    # Input validation
    if number is None:
        raise HTTPException(status_code=400, detail={"number": "missing", "error": True})
    
    # if not is_numeric(number):
    #     raise HTTPException(status_code=400, detail={"number": number, "error": True})
    # Validate input
    print(number)
    print(is_valid_number(number))
    if not is_valid_number(number):
        return JSONResponse(
            status_code=400,
            content={"error": True, "number": number}
        )
    
    try:
        num = int(number)
    except ValueError:
        return JSONResponse(
            status_code=400,
            content={"error": True, "number": number}
        )
    
    # Calculate all properties
    properties = get_number_properties(num)
    fun_fact = get_fun_fact(num)
    
    return NumberResponse(
        number=num,
        is_prime=is_prime(num),
        is_perfect=is_perfect(num),
        properties=properties,
        digit_sum=get_digit_sum(num),
        fun_fact=fun_fact
    )

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": True, "detail": exc.detail}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)