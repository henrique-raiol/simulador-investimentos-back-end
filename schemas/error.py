from pydantic import BaseModel


class ErrorSchema(BaseModel):
    ''' Define como uma mensagem de erro será representada
    '''
    error_code: int
    message: str

if __name__ == '__main__':
    pass