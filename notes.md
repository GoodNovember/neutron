*** These images are not installers. ***

If you don't have Linux running on a PC, you can use Rufus ( https://rufus.ie/ ) to install the image to a USB stick. 
Also copy the image to another USB stick or a Micro SD card.
Then boot from the USB stick and copy the image to the eMMC using the procedure below.

Boot from a USB or uSD card and use dd to copy the image. Use BIOS settings to change the boot order.
Example: # dd if=/where/you/put/the/image.img of=/dev/mmcblk0 bs=1024k oflag=dsync status=progress

These images have a user 'atomicpi' with an assigned password 'atomicpi'.

It should be noted that 'bare' images are really devoid of quite a bit of useful stuff (samples, Python/Node.JS pin definition libraries, etc.). They usually have only the low-level stuff. 
Pin definitions are present in /usr/lib/atomicpi.sh in all images and can be transformed into other languages as well, not just Python or JavaScript.

Some of the 'bare' images don't come with networking configured as DHCP client by default (looking at you Buster) so you might need to do e.g. "sudo dhclient" for that.