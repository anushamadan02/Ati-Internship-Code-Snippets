from video_reader_utils import VideoReader

def main():
    vr = VideoReader('Ati.mp4')
    print('Num images : {}'.format(vr.num_images))

    n = 0

    _, nth_image = vr.get_nth_image(n) 
    print(nth_image.shape)

main()
