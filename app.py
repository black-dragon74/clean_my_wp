from bs4 import BeautifulSoup
import requests
import json

def run():
    with open('data/urls.txt', 'r') as dataFile:
        mData = dataFile.read()
        mURLS = [url for url in mData.splitlines()]

        # Now for each URL, get it, get image links and then write the links to the file
        counter = 1
        imgCount = 0
        for url in mURLS:
            print("Fetching %s" % url)
            data = requests.get(url).content

            # Soup
            soup = BeautifulSoup(data, 'html.parser')

            # Get all the links
            print("Finding all image tags...")
            imgs = soup.find_all('img')

            # For each image
            imgArr: [str] = []
            for img in imgs:
                imgArr.append(img["src"])
            
            print("Found %d image tags." % len(imgArr))
            imgCount += len(imgArr)

            # Write to file
            with open('out/' + str(counter), 'w+') as outFile:
                for imgPath in imgArr:
                    outFile.write("%s\n" % imgPath)
                
                print("Wrote output of %s to %s" % (url, outFile.name))
                print()
                outFile.close()

            counter += 1
        
        print("Successfully processed %d images across %d pages" % (imgCount, counter - 1))


if __name__ == '__main__':
    run()