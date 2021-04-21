import argparse


def format_text_block(frame_height, frame_width, file_name):
    big_line = ''
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = list(file.readline()[:-1])
            line = ''
            for i in range(frame_height):
                flag = 0
                for j in range(frame_width):
                    if len(data) > 0:
                        line += data.pop(0)
                        # print(data.pop(0), end='')
                    else:
                        flag = 1
                        data = list(file.readline()[:-1])
                        break
                big_line += line
                big_line += '\n'
                if len(data) == 0 and flag == 0:
                    data = list(file.readline()[:-1])
                line = ''
            big_line = ''.join(list(big_line)[:-1])
            return big_line
    except Exception as e:
        return e


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--frame-height', dest='fh', type=int, nargs='?')
    parser.add_argument('--frame-width', dest='fw', type=int, nargs='?')
    parser.add_argument('file_name', type=str, nargs='?')

    args = parser.parse_args()

    print(format_text_block(args.fh, args.fw, args.file_name))