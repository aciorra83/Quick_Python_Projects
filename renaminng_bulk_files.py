import os

# creating a function to iterate through files in a specific directory
def main():
    i = 0
# specifying with dir with absolute path
    path = '/home/alex/random_images/'
    # creating a for loop to iterate through the dir
    for filename in os.listdir(path):
        my_img = 'img' + str(i) + '.jpg'
        my_source = path + filename
        my_img = path + my_img
        os.rename(my_source, my_img)
        i += 1
if __name__ == '__main__': 
    main()