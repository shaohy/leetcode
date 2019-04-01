class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        real_email_set = set()
        for i in emails:
            i = i.split("@")
            local_name = i[0]
            domain_name = i[1]
            local_name.split("+")
            local_name = local_name[0]
            local_name.strip(".")
            real_email = local_name + domain_name
            real_email_set.add(real_email)

        return len(real_email_set)
