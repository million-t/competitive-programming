class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        
        
        items = set()
        tables = defaultdict(lambda: defaultdict(int))
        
        for customer, table, item in orders:
            items.add(item)
            tables[table][item] += 1
        
        
        
        ans = [['Table']]
        ans[0].extend(sorted(items))
        
        for table in sorted(tables.keys(), key= lambda x: int(x)):
            row = [table]
            
            for ind in range(1, len(ans[0])):
                item = ans[0][ind]
                row.append(str(tables[table][item]))
            ans.append(row)
            
        return ans
        
        
        
            