*dsl-wall* is an IRC client setup which auto starts on a Raspberry Pi
Zero. On certain user actions, hooks are executed. They trigger
devices in the space, such as the lights or a printer.

See also our wiki entry about [IRC][1].


Setup
=====
 
 1. Make sure that [Smuxi][2], X, and Ratpoison are installed.

 2. Enable auto login on the Rasperry Pi.

 3. Install the `Adwaita-dark` theme into:
 
        ~/.themes/Adwaita-dark
 
 4. Clone to: `~/dsl-wall`
 
 5. Link configuration:
 
        ln -s ~/dsl-wall/.bash_profile ~
        ln -s ~/dsl-wall/.gtkrc-2.0 ~
        ln -s ~/dsl-wall/.xsession ~
        ln -s ~/dsl-wall/smuxi_config ~/.config/smuxi
        ln -s ~/dsl-wall/smuxi_hooks/* \
            ~/.local/share/smuxi/hooks/engine/protocol-manager
            
 6. Install `lprng`:
 
        sudo apt install lprng

    And create `/etc/printcap` for our [printer][3]:
 
        lq590|localprinter:\
        :lp=/dev/usb/lp0:\
        :sd=/var/spool/lpd/lq590:\
        :mx#0:\
        :sh:

    Followed by:
    
        sudo service lprng restart
            
            
DND
===

The idea of DND, the do-not-disturb mode, is to turn off the blinking
for a while. It needs to be activated from the command line from the
directory `smuxi_scripting_fun`.

[1]: https://wiki.dimsumlabs.com/IRC
[2]: https://smuxi.im/
[3]: https://wiki.dimsumlabs.com/Computer-Lab
