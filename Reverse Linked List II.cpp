/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *reverseBetween(ListNode *head, int m, int n) {
        ListNode *ppm = NULL;
        ListNode *pm = head;
        for(int i = 0; i < m-1; i++)
        {
            ppm = pm;
            pm = pm->next;
        }
        ListNode *pn = pm;
        for(int i = m; i <= n; i++)
            pn = pn->next;
        ListNode *pi = pm->next;
        pm->next = pn;
        while(pi != pn)
        {
            ListNode *tmp = pi->next;
            pi->next = pm;
            pm = pi;
            pi = tmp;
        }
        if(!ppm)
            return pm;
        ppm->next = pm;
        return head;
    }
};