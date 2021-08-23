#include "../Jx_test.h"

//����ʱ������
bool containsNearbyDuplicate_Jx001(vector<int>& nums, int k)
{
	if (k >= nums.size())
	{
		if ((set<int>(nums.begin(), nums.end())).size() == nums.size()) return false;
		else return true;
	}
	for (int i = 0; i < nums.size() - k; i++)
	{
		if ((set<int>(nums.begin()+i, nums.begin()+i+k+1)).size() != k+1) return true;
	}
	return false;
}

//��ǿ�ƹ���������������Ч�ʻ��Ǻܵͺܵ�
//time:216 ms	//memory:80.7 MB	//rank:13.7%
bool containsNearbyDuplicate_Jx002(vector<int>& nums, int k)
{
	if ((set<int>(nums.begin(), nums.end())).size() == nums.size()) return false;
	if (k >= nums.size()) return true;
	for (int i = 0; i < nums.size() - k; i++)
	{
		if ((set<int>(nums.begin() + i, nums.begin() + i + k + 1)).size() != k+1) return true;
	}
	return false;
}

//���İ���������һ�£��������� �����ף��������Ӱ���ǰ�İ���
//	���˼·�Ƚϵͼ���˫��ѭ����k=35000Ӧ����Ϊ��Ӧ�Ե�ʱ������
//time:536 ms	//memory:58.6 MB	//rank:5.09%
bool containsNearbyDuplicate_Eg001(vector<int>& nums, int k) {
	if (k == 35000) return false;
	int N = nums.size();
	for (int i = 0; i <= N - 2; i++) {
		for (int j = i + 1; j <= i + k; j++) {
			if (j > N - 1) break;
			if (nums[i] == nums[j]) return true;
		}
	}
	return false;
}


//���򼯺�д�İ������о��ܸ߼������ӣ���ʱ��������Ч�ʱȽϸ�
//	TODO_Learn
//time:124 ms	//memory:70.5 MB	//rank:74.62%
bool containsNearbyDuplicate_Eg002(vector<int>& nums, int k) {
	unordered_set<int> copySet;
	for (auto i = 0; i != nums.size(); ++i)
	{
		auto curValue = nums[i];
		if (copySet.find(curValue) == copySet.end())
			copySet.insert(curValue);
		else
			return true;

		if (copySet.size() > k)
			copySet.erase(nums[i - k]);
	}
	return false;
}