import os

PATH_TO_DATASET = '../dataset/'
def get_video_paths(path=PATH_TO_DATASET):
    paths_to_folders = [x[0] for x in os.walk(path)].remove(path)
    result ={"S":[], "I":[], "C":[]}
    for folder in paths_to_folders:
        last_let = folder[-1]
        if last_let == "S":
            result["S"].append(os.path.join(folder, 'cam0#017.avi'))
        elif last_let == "C":
            result["C"].append(os.path.join(folder, 'cam0#017.avi'))
        else:
            result["I"].append(os.path.join(folder, 'cam0#017.avi'))
    return result