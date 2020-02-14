from util.MongoClient import localClient
from CryptoDataDownloader import CryptoDataDownloader


def getMongoCollection():
    return localClient.crypto.crypto


def updateData(collection, newData):
    coin = newData.name
    collection.update_one({'name': coin}, newData)


if __name__ == '__main__':
    dataDownloader = CryptoDataDownloader()
    collection = getMongoCollection()
    for data in dataDownloader.getTokenData():
        updateData(collection, data)
