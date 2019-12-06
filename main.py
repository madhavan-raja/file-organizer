import os
import time

SLEEP_TIME = 10

category = {
    'exe': 'Applications',
    'jpeg': 'Images',
    'jpg': 'Images',
    'mp3': 'Music',
    'mp4': 'Videos',
    'pdf': 'Documents',
    'zip': 'Archives'
}

other_category = 'Other'


def main():
    print(f'Current directory: {os.getcwd()}')
    print(f'Checking at an interval of {SLEEP_TIME} seconds.')
    print('Press [Ctrl] + [C] to quit.')
    print()

    try:
        while True:
            organize()
            time.sleep(SLEEP_TIME)
    except KeyboardInterrupt:
        print('Quitting.')


def organize():
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f != os.path.basename(__file__)]

    for file in files:
        ext = os.path.splitext(file)[1][1:]
        folder_name = category.get(ext, other_category)
        
        if not os.path.isdir(folder_name):
            os.mkdir(folder_name)

        os.replace(file, os.path.join(folder_name, file))

    if len(files) > 0:
        print(f'Found {len(files)} new file(s).')

if __name__ == '__main__':
    main()