class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_emails = set()
        for i in emails:
            names = i.split("@")
            local_name = names[0]
            domain_name = names[1]
            local_name = local_name.split("+")[0]
            local_name = local_name.replace(".", "")
            unique_emails.add(local_name + "@" + domain_name)
        return len(unique_emails)
