import boto3

# '8593/E_sp010_LensFogging_v4.1159.exr'
# input('Please input Number of assets: ')

#Ask for assets number
filename = input('Please input NUMBER of assets: ')

s3 = boto3.resource('s3')
my_bucket = s3.Bucket('mpc-sharepipe-production-assets-storage')

## Download assets using number 
#Empty list to check if assets exists in S3 bucket
for_download = []
for my_bucket_object in my_bucket.objects.all():
    #Check if key start with input number and download
    if my_bucket_object.key.startswith(filename):
        for_download.append(my_bucket_object.key)
        name = my_bucket_object.key
        name2 = name.split('/')
        my_bucket.download_file(name, name2[1])

# If for_download is empty return false and download for another s3 bucket
if not for_download:
    print("Assets not in mpc-sharepipe-production-assets-storage bucket!")
    filename = input('Please input NAME of assets: ')
    input_split = filename.split("_")

    my_bucket2 = s3.Bucket('dev-share-library')

    first_two_words = ["cg_effects", "guns_n_ammo",
                       "lensflare_light_electricity", "library_elements",
                       "skies_cityscapes", "technical_graphics", "test_category", "tv_film_fx"]

    secend_two_words = ['nuke_gizmo', 'factory_workers', 'blowing_grass', 'on_ground', 'cigarette_lighter',
                        'falling_paper', 'muzzle_flash', 'cinegrain_special', 'circles_of_confusion', 'dirt_on_lens', 'sunlight_on_water',
                        'cities_buildings', 'lake_water', 'wadi_rum', 'puffs_plumes', 'smoke_trail', 'test_subcategory', 'brick_textures',
                        'drap_cine', 'rock_textures', 'cinegrain_flash', 'cinegrain_looks', 'good_grain', 'leaders_countdowns', 'cg_breaking_wave', 'rushing_water']

    first_word = [x for x in first_two_words if input_split[1] in x]

    if not first_word:
        first_word.append(input_split[1])

    split_first_word = str(first_word).split("_")
    l = len(split_first_word) + 1

    secend_word = [x for x in secend_two_words if input_split[l] in x]
    if not secend_word:
        secend_word.append(input_split[l])

    for my_bucket_object in my_bucket2.objects.filter(Prefix=f"jobs/mpcAdvelements_1800417/{first_word[0]}/{secend_word[0]}/elements/"):
        if filename in my_bucket_object.key:
            name = my_bucket_object.key
            name2 = name.split('/')
            my_bucket2.download_file(name, name2[-1])


# first aws s3 cp --recursive s3://pipevfx-help C:\Users\micha\S3test\Download

# Aws cli command:   aws s3 sync s3://pipevfx-help C:\Users\micha\S3test\Download

# AWS With sort aws s3 cp s3://dev-share-library/jobs/mpcAdvelements_1800417/technical_graphics/gfx/elements/LE_technical_graphics_gfx_001_v001/1920x1080/ C:\Users\micha\S3test\Download --recursive --exclude "*" --include "*v001.100*"
