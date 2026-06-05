class Config:
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:password@localhost/finanzas"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
