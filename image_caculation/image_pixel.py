import json

import io
import struct


def get_image_size(image_byte):
    data = image_byte
    size = len(data)
    height = -1
    width = -1
    content_type = ''

    # handle GIFs
    if (size >= 10) and data[:6] in (b'GIF87a', b'GIF89a'):
        # Check to see if content_type is correct
        content_type = 'image/gif'
        w, h = struct.unpack(b"<HH", data[6:10])
        width = int(w)
        height = int(h)

    # See PNG 2. Edition spec (http://www.w3.org/TR/PNG/)
    # Bytes 0-7 are below, 4-byte chunk length, then 'IHDR'
    # and finally the 4-byte width, height
    elif ((size >= 24) and data.startswith(b'\211PNG\r\n\032\n')
          and (data[12:16] == b'IHDR')):
        content_type = 'image/png'
        w, h = struct.unpack(b">LL", data[16:24])
        width = int(w)
        height = int(h)

    # Maybe this is for an older PNG version.
    elif (size >= 16) and data.startswith(b'\211PNG\r\n\032\n'):
        # Check to see if we have the right content type
        content_type = 'image/png'
        w, h = struct.unpack(b">LL", data[8:16])
        width = int(w)
        height = int(h)

    # handle JPEGs
    elif (size >= 2) and data.startswith(b'\377\330'):
        content_type = 'image/jpeg'
        jpeg = io.BytesIO(data)
        jpeg.read(2)
        b = jpeg.read(1)
        try:
            while (b and ord(b) != 0xDA):
                while (ord(b) != 0xFF): b = jpeg.read(1)
                while (ord(b) == 0xFF): b = jpeg.read(1)
                if (ord(b) >= 0xC0 and ord(b) <= 0xC3):
                    jpeg.read(3)
                    h, w = struct.unpack(b">HH", jpeg.read(4))
                    break
                else:
                    jpeg.read(int(struct.unpack(b">H", jpeg.read(2))[0]) - 2)
                b = jpeg.read(1)
            width = int(w)
            height = int(h)
        except struct.error:
            pass
        except ValueError:
            pass

    return {"content_type": content_type, "width": width, "height": height}


def lambda_handler(event, context):
    result = ""
    # hrefs = ['http://farm4.staticflickr.com/3894/15008518202_b016d7d289_m.jpg',
    #          'https://farm4.staticflickr.com/3920/15008465772_383e697089_m.jpg',
    #          'https://farm4.staticflickr.com/3902/14985871946_86abb8c56f_m.jpg',
    #          'http://photos1.blogger.com/blogger/2921/1916/1600/photoshop_apples.jpg']
    # for href in hrefs:
    #     req = requests.get(href)
    #     im = get_image_info(req.content)
    #     result += f"{im[0]}, {im[1]}, {im[2]}\n"

    with open("photoshop_apples.jpeg", "rb") as f:
        im = get_image_info(f.read())
        result += f"{im[0]}, {im[1]}, {im[2]}\n"

    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }




