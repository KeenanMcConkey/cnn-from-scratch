# CNN from the ground up
# Author: Keenan McConkey

def convolution(image, filters, bias, s=1):
    '''
    Convolve 'filters' over 'image' using stride 's', adding 'bias'

    Input:
        image - Input image to convolve over (NumPy Array)
        filters - Filters to convolve with (NumPy Array)
        bias - Bias to add (scalar)
        s - Stride, how far to move filter after each convolve (scalar)
    Output:
        Output array of convolution result for each filter
    '''

    # Num filters x Num filter channels x Filter dimension x Filter dimension
    f_n, f_ch, f_dim, _ = filters.shape
    # Num image channels x Image dimension x Image dimension
    i_ch, i_dim, _ = image.shape

    # Assert same number of filter channels and image channels
    assert f_ch == i_ch

    # Num filters x Output dimension x Output dimension
    o_dim = int( (i_dim - f_dim) / s ) + 1
    output = np.zeros( (n_f, o_dim, o_dim) )

    # Convolve each filter over image
    for f in range(f_n):
        # Move filter vertically across image
        i_y = o_y = 0
        while i_y + f_dim <= i_dim:
            # Move filter horizontally across image
            i_x = o_x = 0
            while i_x + f <= i_dim:
                # Convolution operation plus bias
                output[f, o_y, o_x] = np.sum( filter[f] * image[:, i_y:i_y+f_dim, i_x:i_x+f_dim] ) + bias[f]
                i_x += s
                o_x += 1
            i_y += s
            o_y += 1

    return output

def maxpool(image, k=2, s=2):
    '''
    Downsample 'image' using a kernel of size 'k' and stride of 's'

    Input:
        image - To be downsampled (NumPy array)
        k - Kernel size (scalar)
        s - Stride, how far to move filter after each convolve (scalar)
    Output:
        Downampled image after maxpooling operation (NumPy array)
    '''
    # Num image channels x Image height x Image width
    n_ch, i_h, i_w = image.shape

    # Num image channels x Output hweight x Output width
    o_h = int( (i_h - k) / s ) + 1
    o_w = int( (i_w - k) / s ) + 1
    output = np.zeros((n_ch, o_h, o_w))

    # Slide maxpooling kernel over image using stride 's'
    for ch in range(n_ch):
        # Move kernel vertically across image
        i_y = o_y = 0
        while i_y + k <= i_h:
            # Move kernel horizontally across image
            i_x = o_x = 0
            while i_x + k <= i_w:
                # Apply maxpool operation and store in output array
                output[ch, o_y, o_x] = np.max( image[i, i_y:i_y+k, i_x:i_x+k] )
                i_x += s
                o_x += 1
            i_y += s
            i_x += 1

    return output
