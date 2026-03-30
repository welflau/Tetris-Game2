# 架构设计 - 音效系统开发

## 架构模式
模块化架构（Module Pattern）

## 技术栈

- **language**: JavaScript ES6+
- **framework**: 原生HTML5 Web Audio API
- **database**: LocalStorage（音效设置存储）
- **others**: Web Audio API, Audio Context, Buffer Source, Gain Node

## 模块设计

### AudioManager
职责: 音效系统核心管理器，负责音频上下文初始化、音效加载、播放控制和音量管理
- init()
- loadSound(name, url)
- playSound(name, volume)
- setMasterVolume(volume)
- mute()
- unmute()

### SoundLoader
职责: 音效资源加载器，负责音频文件的异步加载、解码和缓存管理
- loadAudioFile(url)
- decodeAudioData(arrayBuffer)
- getCachedSound(name)
- preloadSounds(soundList)

### SoundPlayer
职责: 音效播放器，负责具体音效的播放、停止和音量控制
- play(audioBuffer, volume)
- stop()
- setVolume(volume)
- createGainNode()

### GameSoundEvents
职责: 游戏音效事件处理器，定义和管理各种游戏事件对应的音效触发
- onPieceMove()
- onPieceRotate()
- onPieceDrop()
- onLineClear()
- onGameOver()
- onLevelUp()

### AudioSettings
职责: 音效设置管理器，负责用户音效偏好的存储和读取
- saveSetting(key, value)
- loadSetting(key)
- resetToDefault()
- exportSettings()
- importSettings()

## 数据流
用户操作触发游戏事件 -> GameSoundEvents监听事件 -> 调用AudioManager播放对应音效 -> SoundPlayer创建音频源节点 -> 通过GainNode控制音量 -> 输出到AudioContext进行播放，同时AudioSettings负责持久化用户的音效设置偏好

## 风险点
- 浏览器音频自动播放策略限制，需要用户交互后才能播放
- 不同浏览器对Web Audio API支持程度不一致
- 音频文件加载失败或格式不支持的兼容性问题
- 移动设备音频延迟和性能问题
- 音频文件大小影响加载速度和带宽消耗

## 关键决策
- 使用Web Audio API而非HTML5 Audio元素，以获得更好的性能和控制能力
- 采用音频缓冲区预加载策略，避免播放时的延迟
- 实现音效池机制，支持同一音效的并发播放
- 使用GainNode实现精细的音量控制和淡入淡出效果
- 音效文件采用OGG和MP3双格式支持，确保浏览器兼容性
- 实现用户首次交互时的音频上下文激活机制
