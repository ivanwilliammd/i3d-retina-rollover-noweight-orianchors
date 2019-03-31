"""
Copyright 2017-2018 Fizyr (https://fizyr.com)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import tensorflow


def ones(*args, **kwargs):
    """ See https://www.tensorflow.org/versions/master/api_docs/python/tf/ones .
    """
    return tensorflow.ones(*args, **kwargs)


def transpose(*args, **kwargs):
    """ See https://www.tensorflow.org/versions/master/api_docs/python/tf/transpose .
    """
    return tensorflow.transpose(*args, **kwargs)


def map_fn(*args, **kwargs):
    """ See https://www.tensorflow.org/versions/master/api_docs/python/tf/map_fn .
    """
    return tensorflow.map_fn(*args, **kwargs)


def pad(*args, **kwargs):
    """ See https://www.tensorflow.org/versions/master/api_docs/python/tf/pad .
    """
    return tensorflow.pad(*args, **kwargs)


def top_k(*args, **kwargs):
    """ See https://www.tensorflow.org/versions/master/api_docs/python/tf/nn/top_k .
    """
    return tensorflow.nn.top_k(*args, **kwargs)


def clip_by_value(*args, **kwargs):
    """ See https://www.tensorflow.org/versions/master/api_docs/python/tf/clip_by_value .
    """
    return tensorflow.clip_by_value(*args, **kwargs)

# def resize3d(images, size, method='bilinear', align_corners=False):
#     # define resized_image
#     resized_list = []


#     if is_grayscale:
#         unstack_img_depth_list = [tf.expand_dims(x,2) for x in tf.unstack(image, axis = ax)]
#         for i in unstack_img_depth_list:
#             resized_list.append(tf.image.resize_images(i, [dim_1, dim_2],method=0))
#         stack_img = tf.squeeze(tf.stack(resized_list, axis=ax))
#         print(stack_img.get_shape())

#     else:
#         unstack_img_depth_list = tf.unstack(image, axis = ax)
#         for i in unstack_img_depth_list:
#             resized_list.append(tf.image.resize_images(i, [dim_1, dim_2],method=0))
#         stack_img = tf.stack(resized_list, axis=ax)

#     return stack_img

# resized_along_depth = resize_by_axis(x,50,60,2, True)
# resized_along_width = resize_by_axis(resized_along_depth,50,70,1,True)
#     return resized_image

def resize_images(images, size, method='bilinear', align_corners=False):
    """ See https://www.tensorflow.org/versions/master/api_docs/python/tf/image/resize_images .

    Args
        method: The method used for interpolation. One of ('bilinear', 'nearest', 'bicubic', 'area').
    """
    methods = {
        'bilinear': tensorflow.image.ResizeMethod.BILINEAR,
        'nearest' : tensorflow.image.ResizeMethod.NEAREST_NEIGHBOR,
        'bicubic' : tensorflow.image.ResizeMethod.BICUBIC,
        'area'    : tensorflow.image.ResizeMethod.AREA,
    }
    return tensorflow.image.resize_images(images, size, methods[method], align_corners)
    # return resize3d(images, size, methods[method], align_corners)


def non_max_suppression(*args, **kwargs):
    """ See https://www.tensorflow.org/versions/master/api_docs/python/tf/image/non_max_suppression .
    """
    return tensorflow.image.non_max_suppression(*args, **kwargs)


def range(*args, **kwargs):
    """ See https://www.tensorflow.org/versions/master/api_docs/python/tf/range .
    """
    return tensorflow.range(*args, **kwargs)


def scatter_nd(*args, **kwargs):
    """ See https://www.tensorflow.org/versions/master/api_docs/python/tf/scatter_nd .
    """
    return tensorflow.scatter_nd(*args, **kwargs)


def gather_nd(*args, **kwargs):
    """ See https://www.tensorflow.org/versions/master/api_docs/python/tf/gather_nd .
    """
    return tensorflow.gather_nd(*args, **kwargs)


def meshgrid(*args, **kwargs):
    """ See https://www.tensorflow.org/versions/master/api_docs/python/tf/meshgrid .
    """
    return tensorflow.meshgrid(*args, **kwargs)


def where(*args, **kwargs):
    """ See https://www.tensorflow.org/versions/master/api_docs/python/tf/where .
    """
    return tensorflow.where(*args, **kwargs)