# Sublime Text 2

[Setting up Sublime Text for Python development](https://dbader.org/blog/setting-up-sublime-text-for-python-development)

##Installation

###apt-get method

[Install via the Package Manager(apt-get)](http://askubuntu.com/questions/172698/how-do-i-install-sublime-text-2-3)

```bash
sudo add-apt-repository ppa:webupd8team/sublime-text-2
sudo apt-get update
sudo apt-get install sublime-text
```

###Open Sublime Text 2 from bash shell

Just copy and paste:

```bash
ln -s /Applications/Sublime\ Text\ 2.app/Contents/SharedSupport/bin/subl /usr/local/bin/subl
```
Then you can use `subl` in bash to open it.

##Package control

###Installation

It is a very handy tool to manage the packages for Sublime Text. Install it for your Sublime Text using with the [link](https://packagecontrol.io/installation#Simple) here.

###Some useful packages

Below are some packages I installed:
```jason
"installed_packages":
[
	"All Autocomplete",
	"Package Control",
	"SublimeCodeIntel",
	"Theme - Soda",
	"Tomorrow Color Schemes"
]
```
I haven't tried all out yet.

###Configuration

Click `Preferences > setting-User`, paste the following code in `Preferences.sublime-settings`, and you'll get a nice UI for future coding.

```json
{
	"auto_complete": false,
	"caret_style": "solid",
	"color_scheme": "Packages/Tomorrow Color Schemes/Tomorrow-Night.tmTheme",
	"draw_white_space": "all",
	"ensure_newline_at_eof_on_save": true,
	"file_exclude_patterns":
	[
		".DS_Store",
		"*.pid",
		"*.pyc"
	],
	"find_selected_text": true,
	"fold_buttons": false,
	"folder_exclude_patterns":
	[
		".git",
		"__pycache__",
		"env",
		"env3"
	],
	"font_face": "Ubuntu Mono",
	"font_options":
	[
		"subpixel_antialias",
		"no_bold"
	],
	"font_size": 16.0,
	"highlight_line": true,
	"highlight_modified_tabs": true,
	"ignored_packages":
	[
		"Vintage"
	],
	"line_padding_bottom": 0,
	"line_padding_top": 0,
	"rulers":
	[
		72,
		79
	],
	"scroll_past_end": false,
	"show_full_path": true,
	"show_minimap": false,
	"tab_size": 4,
	"translate_tabs_to_spaces": true,
	"trim_trailing_white_space_on_save": true,
	"wide_caret": true,
	"word_wrap": true,
	"wrap_width": 80
}
```



	
