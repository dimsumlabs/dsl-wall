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
 
 5. Set up configuration:
 
        ln -s ~/dsl-wall/.bash_profile ~
        ln -s ~/dsl-wall/smuxi_scripting_fun ~
        ln -s ~/dsl-wall/.gtkrc-2.0 ~
        ln -s ~/dsl-wall/.xsession ~
        ln -s ~/dsl-wall/smuxi_config ~/.config/smuxi

 6. Symlink the Smuxi hooks into: `~/.local/share/smuxi/hooks/`

[1]: https://wiki.dimsumlabs.com/IRC
[2]: https://smuxi.im/
