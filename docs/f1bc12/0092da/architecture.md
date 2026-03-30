# 架构设计 - 音效系统开发

## 架构模式
观察者模式 + 策略模式

## 技术栈

- **language**: JavaScript ES6+
- **framework**: Web Audio API
- **database**: LocalStorage
- **others**: HTML5 Audio, AudioContext, 音频文件格式(MP3/OGG/WAV)

## 模块设计

### AudioManager
职责: 音效系统核心管理器，负责音频资源加载、播放控制、音量管理
- loadAudio()
- playSound()
- stopSound()
- setVolume()
- muteAll()
- preloadAssets()

### SoundPool
职责: 音频对象池管理，复用Audio实例，避免频繁创建销毁
- getAudioInstance()
- releaseAudioInstance()
- createPool()
- clearPool()

### AudioLoader
职责: 音频资源异步加载器，支持多种格式，处理加载失败
- loadAudioFile()
- checkAudioSupport()
- getOptimalFormat()
- onLoadComplete()

### SoundEffects
职责: 游戏音效枚举和配置，定义各种音效类型和参数
- MOVE_SOUND
- ROTATE_SOUND
- DROP_SOUND
- LINE_CLEAR_SOUND
- GAME_OVER_SOUND
- LEVEL_UP_SOUND

### AudioSettings
职责: 音频设置管理，包括音量控制、静音状态、用户偏好
- saveSetting()
- loadSetting()
- toggleMute()
- setMasterVolume()
- setSFXVolume()

### GameAudioIntegration
职责: 游戏事件与音效的集成层，监听游戏事件触发对应音效
- bindGameEvents()
- onBlockMove()
- onBlockRotate()
- onLineClear()
- onGameOver()

## 数据流
游戏事件触发 -> GameAudioIntegration监听 -> AudioManager处理音效请求 -> SoundPool获取音频实例 -> Web Audio API播放音效 -> AudioSettings控制音量和静音状态 -> LocalStorage保存用户音频偏好

## 风险点
- 不同浏览器音频格式兼容性问题
- 移动设备音频自动播放限制
- 音频文件加载失败或网络延迟
- 频繁音效播放可能造成性能问题
- 音频文件大小影响游戏加载速度

## 关键决策
- 使用Web Audio API提供更好的音频控制和性能
- 实现音频对象池避免频繁创建Audio对象
- 支持多种音频格式确保跨浏览器兼容性
- 采用异步加载和预加载策略优化用户体验
- 使用观察者模式解耦游戏逻辑和音效系统
- 提供完整的音频设置选项满足用户需求
