import os
import shutil




def main():
    try:

        path = 'C:\\Users\\ankan\\Desktop\\Datasets_Healthy_Older_People\\S1_dataset'
        files = os.listdir(path)


        path1 = 'C:\\Users\\ankan\\Desktop\\Datasets_Healthy_Older_People\\S2_dataset'
        files1 = os.listdir(path1)
        
        for index, file in enumerate(files):
            if not os.path.exists(os.path.join(path, file)):
                os.rename(os.path.join(path, file), os.path.join(path, ''.join([str(index), '.csv'])))
            if not os.path.exists(os.path.join(path1, file)):
                for index, file in enumerate(files1):
                    os.rename(os.path.join(path1, file), os.path.join(path1, ''.join([str(index), '.csv'])))




    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()