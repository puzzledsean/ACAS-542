import requests
import shutil
import os

def download_file(url):
    '''
    https://stackoverflow.com/questions/16694907/how-to-download-large-file-in-python-with-requests-py
    '''
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        shutil.copyfileobj(r.raw, f)

    return local_filename

def scrape():
    '''
    Iterate through dates and numbers to download from opensky-network
    '''

    dates = ['2017-08-28', '2017-09-04','2017-09-11', '2017-09-18', '2017-09-25', '2017-10-02', '2017-10-09', '2017-10-16', '2017-10-23',
      '2017-10-30', '2017-11-06']
    nums = [x for x in range(24)]
    nums = ['0' + str(x) if x < 10 else str(x) for x in nums]
    BASE_URL = 'https://opensky-network.org/datasets/states/{date}/{num}/states_{date}-{num}.csv.tar'

    for date in dates:
        
        print('========================================================================')
        print('============ Date: {}'.format(date))
        for num in nums:
            fname = 'states_{}-{}.csv.tar'.format(date, num)
            if os.path.isfile(fname):
                print('Skipping. File {} already exists...'.format(fname))
                continue

            print('-------')
            download_url = BASE_URL.format(date=date, num=num)
            print('About to download date: {}, number: {}...'.format(date, num))
            try:
                download_file(download_url)
                print('Successfully downloaded date: {}, number: {}'.format(date, num))
            except KeyboardInterrupt:
                print('quitting')
                return
            except:
                print('error downloading date: {}, number: {}'.format(date, num))
            print('-------')
        print('========================================================================')

scrape()
