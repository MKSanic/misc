import os
import shutil
def convert_to_mp4(mkv_file):
    name, ext = os.path.splitext(mkv_file)
    out_name = 'mp4s/' + name + ".mp4"
    os.system(f'ffmpeg -i {mkv_file} -codec copy {out_name}')
    shutil.move(mkv_file,'mkvs/' + mkv_file)
    print("Finished converting {}".format(mkv_file))
start_dir='./'
for path, folder, files in os.walk(start_dir):
    for file in files:
        if file.endswith('.mkv'):
            print("Found file: %s" % file)
            convert_to_mp4(os.path.join(start_dir, file))
        else:
            pass
input()

