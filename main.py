if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.main:app",reload=True, port=8000)