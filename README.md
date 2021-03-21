# yao-bridge

Bridging messages among Yao groups

![SayNoToWeChat](https://i.imgur.com/dCZfh14.png)

## TERMS OF SERVICE (V1.0)

1. 本服务可能会保存用户的信息，包括但不限于用户的 ID（包括用户名，群内昵称，Sharzy 对该用户的备注），消息内容。由于架构的原因，这些信息可能会保存在 Sharzy 个人的服务器以及 Telegram 的服务器上。
2. 我们不对服务有任何保证，我们也不对服务产生的任何后果负责。我们可能在任何时候停止、暂停或维护该服务，由于个人或者微信端的原因。
3. 目前本服务不支持消息的撤回，也不支持红包等微信高级功能。我们稍后会对本项目的架构和代码进行说明和开源。有兴趣的同学可以自行研发撤回等功能。

## TODO LIST

1. 我们的服务支持任意多的群组，我们可能会在未来加入 Telegram 群组「姚班后花园」的支持。
2. 我们的服务需要一个更科学的架构，目前运营在个人帐号上，未来可能运营在更科学的帐号上。

## Architecture

我们依赖如下服务：

1. [EFB bot](https://github.com/ehForwarderBot/)
2. [Telethon](https://github.com/LonamiWebs/Telethon/)

我们用第一个工具搭建了一个 WeChat bot，它可以将微信端的所有支持的消息转发到 Telegram 上，也可以将 Telegram 的某些信息转发回到微信中。同时也可以将微信某个群组的消息转发到特定的 Telegram 群组中。我们又使用第二个工具搭建了一个 user bot，该 bot 实现了将一个 Telegram 群组的消息转发到另一个 Telegram 群组的功能（目前的设计下可以转发任意多的群组）。

在这两个 bot 的帮助下，我们新建了两个 Telegram 群组，分别对应（微信上的）大群和二群，我们令 WeChat Bot 将两个微信群的消息分别转发到这两个 Telegram 群组中，然后使用 user bot 转发这两个群的消息，这两个群的消息便会被 WeChat bot 转发回微信端，实现微信两个群的消息同步。

## Deployment

我们的 WeChat Bot 是按照 [efb-wechat-slave](https://github.com/ehForwarderBot/efb-wechat-slave/) 中提供的方式部署的。

我们的 user bot 代码位于项目的 [userbot.py](userbot.py) 中。注意需要自行填写相关的参数。

## Credit

Design: [Zenithal](https://github.com/ZenithalHourlyRate/)

