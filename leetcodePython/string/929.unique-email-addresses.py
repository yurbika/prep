class Solution:
    def isValid(self, email):
        string = email.split('@')
        string[0] = string[0].split('+')[0]
        string[0] = string[0].replace('.', '')
        return string[0] + '@' + string[1]

    def numUniqueEmails(self, emails: List[str]) -> int:
        for i in range(len(emails)):
            s = emails.pop(0)
            s = self.isValid(s)
            if s not in emails:
                emails.append(s)
        return len(emails)
