class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        import collections

        color_freq_ord = list(sorted(collections.Counter(colors).items(), reverse=True, key=lambda kv: kv[1]))

        num_nodes = len(colors)
        tbl_forward_edges = [[] for _ in range(num_nodes)]
        for src, dest in edges:
            tbl_forward_edges[src].append(dest)

        class CycleError(ValueError):
            pass
        
        def find_max_color_path(target_color):
            INIT = 0
            RUNNING = 1
            DONE = 2
            tbl_search_state = [INIT for _ in range(num_nodes)]
            tbl_max_cnts = [0 for _ in range(num_nodes)]

            def count_matched_dfs(root: int):
                root_state = tbl_search_state[root]
                if root_state == RUNNING:
                    raise CycleError()
                if root_state == DONE:
                    return tbl_max_cnts[root]
                assert root_state == INIT
                tbl_search_state[root] = RUNNING
                max_cnts = 0
                for node in tbl_forward_edges[root]:
                    if tbl_search_state[node] == INIT:
                        sub_cnts = count_matched_dfs(node)
                    elif tbl_search_state[node] == DONE:
                        sub_cnts = tbl_max_cnts[node]
                    else:
                        raise CycleError()
                    max_cnts = max(sub_cnts, max_cnts)

                max_cnts += int(colors[root] == target_color)
                tbl_max_cnts[root] = max_cnts
                tbl_search_state[root] = DONE
                return max_cnts

            max_cnts = 0
            for root in range(num_nodes):
                max_cnts = max(count_matched_dfs(root), max_cnts)
            return max_cnts

        max_cnts = 0
        for target_color, freq in color_freq_ord:
            if freq < max_cnts:
                break
            try:
                max_cnts = max(find_max_color_path(target_color), max_cnts)
            except CycleError:
                return -1
        return max_cnts