import boto3

# 6148 asset not in bucket
# LE_guns_n_ammo_muzzle_flash_002 name of 6148
# '8593/E_sp010_LensFogging_v4.1159.exr'
# input('Please input Number of assets: ')
# One frame 8246
# 8145 small


def get_input():
    key_f = input(
        """
    How do you want download asset:
        A: With selected key keyframe.
        B: Whole asset.
        Pleace enter a or b: """
    )
    if key_f.lower() == "a":
        keyframes = []
        s_keyframe = input("Please enter start keyframe: ")
        keyframes.append(s_keyframe)
        f_keyframe = input("Please enter end keyframe: ")
        keyframes.append(f_keyframe)
        print("Grate")
        return keyframes
    print("Grate")
    return key_f


def add_to_ready_list():
    if a.lower() != "b":
        for k in for_download:
            kk = k.split(".")
            if kk[1] <= a[1] and kk[1] >= a[0]:
                ready_list.append(k)


def download():
    if ready_list:
        for obcject in ready_list:
            obcject2 = obcject.split("/")
            try:
                my_bucket.download_file(obcject, obcject2[-1])
            except:
                my_bucket2.download_file(obcject, obcject2[-1])
    else:
        for obcject in for_download:
            obcject2 = obcject.split("/")
            try:
                my_bucket.download_file(obcject, obcject2[-1])
            except:
                my_bucket2.download_file(obcject, obcject2[-1])


a = get_input()
# Ask for assets number
filename = input("Please input NUMBER of assets: ")
s3 = boto3.resource("s3")
my_bucket = s3.Bucket("mpc-sharepipe-production-assets-storage")

# Download assets using number
# Empty list to check if assets exists in S3 bucket
for_download = []
ready_list = []
for my_bucket_object in my_bucket.objects.all():
    # Check if key start with input number and download
    if my_bucket_object.key.startswith(filename):
        for_download.append(my_bucket_object.key)

add_to_ready_list()

download()

# If for_download is empty return false and download for another s3 bucket
if not for_download:
    print("Assets not in mpc-sharepipe-production-assets-storage bucket!")
    filename = input("Please input NAME of assets: ")
    input_split = filename.split("_")

    my_bucket2 = s3.Bucket("dev-share-library")
    # The first double word list
    first_two_words = [
        "cg_effects",
        "guns_n_ammo",
        "lensflare_light_electricity",
        "library_elements",
        "skies_cityscapes",
        "technical_graphics",
        "test_category",
        "tv_film_fx",
    ]
    # The secend double word list
    secend_two_words = [
        "nuke_gizmo",
        "factory_workers",
        "blowing_grass",
        "on_ground",
        "cigarette_lighter",
        "falling_paper",
        "muzzle_flash",
        "cinegrain_special",
        "circles_of_confusion",
        "dirt_on_lens",
        "sunlight_on_water",
        "cities_buildings",
        "lake_water",
        "wadi_rum",
        "puffs_plumes",
        "smoke_trail",
        "test_subcategory",
        "brick_textures",
        "drap_cine",
        "rock_textures",
        "cinegrain_flash",
        "cinegrain_looks",
        "good_grain",
        "leaders_countdowns",
        "cg_breaking_wave",
        "rushing_water",
    ]
    # check if input in first_two_words
    first_word = [x for x in first_two_words if input_split[1] in x]

    if not first_word:
        first_word.append(input_split[1])
    # Split first_word to count how many words is in.
    split_first_word = str(first_word).split("_")
    l = len(split_first_word) + 1
    # loop secend list of category
    secend_word = [x for x in secend_two_words if input_split[l] in x]
    if not secend_word:
        secend_word.append(input_split[l])

    for my_bucket_object in my_bucket2.objects.filter(
        Prefix=f"jobs/mpcAdvelements_1800417/{first_word[0]}/{secend_word[0]}/elements/"
    ):
        if filename in my_bucket_object.key:
            for_download.append(my_bucket_object.key)
    add_to_ready_list()

    download()
print("Download Finish!!!")

# first aws s3 cp --recursive S3Bucket name Local path

# Aws cli command:   aws s3 sync S3Bucket name Local path
