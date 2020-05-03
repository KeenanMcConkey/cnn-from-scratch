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
    i_ch, i_dim, i_dim = image.shape

    # Assert same number of filter channels and image channels
    assert f_ch == i_ch

    # Output dimensions (output is conv)
    o_dim = int( (i_dim - f_dim) / s ) + 1
    # Num filters x Output dimension x Output dimension
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
                output[f, o_y, o_x] = np.sum(filter[f] * image[:, i_y:i_y+f_dim, i_x:i_x+f_dim]) + bias[f]
                i_x += s
                o_x += 1
            i_y += s
            o_y += 1

    return output
