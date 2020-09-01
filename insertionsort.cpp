class Solution
{
public:
    ListNode *insertionSortList(ListNode *head)
    {
        int flag = 3;
        ListNode *curr = head;
        ListNode *prev = NULL;
        ListNode *nex = head->next;
        while (curr != NULL)
        {
            ListNode *curr1 = head;
            ListNode *prev1 = NULL;
            ListNode *nex1 = curr1->next;
            while (curr1 != NULL && curr1 != curr)
            {
                // if not sorted
                if (curr1->val > curr->val)
                {
                    //if the node is head
                    if (curr1 == head)
                    {
                        curr->next = head;
                        head = curr;
                        prev->next = nex;

                        flag = 1;
                        break;
                    }
                    // if the greater node is not the head
                    else
                    {
                        prev1->next = curr;
                        curr->next = curr1;
                        flag = 2;
                        break;
                    }
                }
                // if the node is not greater i.e, already sorted
                else
                {
                    flag = 3;
                    prev1 = curr1;
                    curr1 = nex1;
                    nex1 = nex1->next;
                }
            }
            if (flag == 1)
            {
                curr = nex;
                nex = nex->next;
            }
            if (flag == 2)
            {
                curr = nex;
                if (nex)
                    nex = nex->next;
            }

            if (flag == 3)
            {
                prev = curr;
                curr = nex;
                if (nex)
                    nex = nex->next;
            }
            flag = 3;
        }
        return head;
    }
}