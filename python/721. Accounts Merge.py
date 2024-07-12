from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        result=defaultdict(set)
        for account in accounts:
            for email in account[1:]:
                result[account[1]].add(email)
                result[email].add(account[1])
        answer=[]
        visited=set()
        for account in accounts:
            if account[1] not in visited:
                name=account[0]
                stack=[account[1]]
                emails=[]
                while stack:
                    node=stack.pop()
                    if node not in visited:
                        visited.add(node)
                        stack.extend(result[node])
                        emails.append(node)
                answer.append([name]+sorted(emails))
        return answer