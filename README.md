# Mentorbot 3.0

A custom Discord bot by the Rivals of Aether Academy.

See Mentorbot in the [Rivals of Aether Academy](https://discord.me/mentor), or [add it to your own server](https://discordapp.com/api/oauth2/authorize?client_id=475596740368793600&permissions=264192&scope=bot).


## Universal Features

### Hitbox Commands

Mentorbot's hitbox commands provide detailed frame data and hitbox images for any move in the game, covering the movesets of all 14 characters.

<img src="https://i.imgur.com/ZMwQbvT.png" align="left"
title="Hitbox Commands" alt="hitbox commands examples" width="800"/><br clear="all"/>

The syntax for these commands is <kbd>![character] [move]</kbd>. Multiple character and move names are supported.

<img src="https://i.imgur.com/vKaR7Oy.png" align="left" 
title="Hitbox Command Demo" alt="hitbox command demo" width="600"/><br clear="all"/>

### Informational Commands

Mentorbot includes a growing list of informational and reference commands, from in-game stats to competitive strategy guides.

<img src="https://i.imgur.com/Hrn6RWt.png" align="left"
title="Info Commands" alt="info commands examples" width="800"/><br clear="all"/>

<kbd>!commands</kbd> provides a full list of available info commands, as seen below.

<img src="https://i.imgur.com/CP9TqoM.png" align="left" 
title="Info Commands List" alt="info commands list" width="400"/><br clear="all"/>

### Server Moderation

#### Action Logging

Track edited and deleted messages, members joining and leaving, and other server actions via Mentorbot's action logging functionality. Enable this feature by creating a channel called <kbd>#action-log</kbd> and ensuring Mentorbot has permissions to send messages.

<img src="https://i.imgur.com/8dbzh9X.png" align="left"
title="Action-Log Examples" alt="action-log examples" width="800"/><br clear="all"/>

#### Commands

<kbd>!whois [member]</kbd> provides detailed information on a given member specified by username, @mention, or user ID. This command is only accessible to those with permissions to ban users.

<img src="https://i.imgur.com/so0HtFk.png" align="left" 
title="!Whois Command" alt="!whois command" width="400"/><br clear="all"/>

<kbd>!clear [n]</kbd> deletes the specified amount of messages from the current chat, and logs this into <kbd>#action-log</kbd>. This command is only accessible to those with permissions to manage messages. To enable this functionality, Mentorbot needs the required permissions to delete messages, and so needs to be invited via [this link](https://discordapp.com/api/oauth2/authorize?client_id=475596740368793600&permissions=272384&scope=bot).

<img src="https://i.imgur.com/W0aTDBd.png" align="left" 
title="!Clear Command" alt="!clear command" width="300"/><br clear="all"/>


## Academy-Specific Features

### Mentor Commands

<img src="https://i.imgur.com/8Iftgz7.png" align="left"
title="Mentor Commands" alt="mentor commands examples" width="800"/><br clear="all"/>

#### Management

![mentor management demo]( "Mentor Management Demo")


### Role Management

![set-your-roles](https://i.imgur.com/fIjcHbz.png "Set-Your-Roles")

#### Moderation

![suspend/unsuspend commands]( "Suspend/Unsuspend Commands")


## Credits

* [Blair C.](https://github.com/blair-c) - *Programming*
* [SNC](https://twitter.com/SNC_Sector7G) @ [Sector 7-G](https://discord.gg/qgKqaPX) - *Frame data info*


## License

[![License](http://img.shields.io/:license-mit-blue.svg)](http://doge.mit-license.org)
* [MIT License](https://opensource.org/licenses/MIT)
* MIT © Blair C.
