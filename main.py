from services.Web3Service import Web3Service
from VideoFeed.VideoProccessing import VideoProcessor
from components.BadgeDroper import BadgeDropper

if __name__ == "__main__":
    w3service = Web3Service('https://dai.poa.network')
    badge_dropper = BadgeDropper(w3service)
    videoFeed = VideoProcessor(0,badge_dropper)
    videoFeed.lookForQR()
    videoFeed.source.release()
    videoFeed.source.destroyAllWindows()