我们令 dfs(curr, prev) 表示以 curr 为根的子树保持healthy时，能够取得的最高分。
我们容易发现，从 root 一路往下时，只要在某个节点 node 采取了“不取”的策略，那么之后就没有继续往下走的必要了。
因为从root到node再到它的任何一个leaf，这个path sum肯定不会是零。所以我们必然会贪心地将 node 以下所有节点的 value 都取走。
所以我们在 dfs 的过程中，如果遍历到了某个节点，其隐含的意思就是从 root 到 node 之间的路径都“扫荡”光了。
此时如果 node 依然采用了“取”的策略，那么我们必须保证 node 的所有子树 path 都是 healthy 的才行。于是就是递归处理 dfs(nxt, curr) 即可。
边界条件是对于leaf node，它必须不取，否则连它也取的话，则意味着从 root 到 leaf 的 path 每个节点都取光了，必然不是 healthy。
