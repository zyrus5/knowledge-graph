# Java

## JVM

* 内存监控工具: [VisualVM](JVM/visualvm.md)
* 导出内存快照
    * jps 查看进程pid
    * jmap -dump:file=xxx.hprof pid
* 导出线程快照
    * jps 查看进程pid
    * jstack [pid]
* 其他工具
    * MAT 堆内存分析工具
    * GChisto GC日志分析工具
    * GCViewer GC日志分析工具

## 限流

| 框架       | Sentinel   | Resilience4j | Guava RateLimiter | Bucket4j   |
|----------|------------|--------------|-------------------|------------|
| 灵活性      | 高，可扩展      | 非常高，模块化      | 低                 | 中等，配置丰富    |
| 监控       | 强大，独立控制台   | 集成外部监控       | 无内置               | 集成外部监控     |
| Spring整合 | 良好，starter | 优秀，注解配置      | 简单                | 良好，starter |
| 轻量级      | 中大型        | 极轻量          | 极轻量               | 较轻量        |

## 状态机

* spring-statemachine
* squirrel
* smart-engine