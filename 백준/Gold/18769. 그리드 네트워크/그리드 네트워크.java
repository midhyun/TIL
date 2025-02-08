import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;

public class Main {

	static class Node{
		int a,b;
		int w;
		public Node(int a, int b, int w) {
			super();
			this.a = a;
			this.b = b;
			this.w = w;
		}
		@Override
		public String toString() {
			return "Node [a=" + a + ", b=" + b + ", w=" + w + "]";
		}

	}
	static int[] parent;
	static int find(int a) {
		if(parent[a]==a)
			return a;

		return parent[a]=find(parent[a]);

	}

	public static void main(String[] args)throws IOException{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		PrintWriter pw= new PrintWriter(System.out);

		int t= Integer.parseInt(br.readLine());

		while(t-->0) {
			int r,c;
			String[] str=br.readLine().split(" ");
			r=Integer.parseInt(str[0]);
			c=Integer.parseInt(str[1]);
			ArrayList<Node> arr=new ArrayList<>();

			for(int i=0;i<r;i++) {
				str=br.readLine().split(" ");
				for(int j=0;j<c-1;j++) {
					int a=i*c+j;
					int b=a+1;
					int w=Integer.parseInt(str[j]);
					arr.add(new Node(a,b,w));
				}
			}
			for(int i=0;i<r-1;i++) {
				str=br.readLine().split(" ");
				for(int j=0;j<c;j++) {
					int a=i*c+j;
					int b=a+c;
					int w=Integer.parseInt(str[j]);
					arr.add(new Node(a,b,w));
				}
			}


			//가중치기준 오름차순 정렬
			Collections.sort(arr,(a,b)->a.w-b.w);

			//사이클존재유뮤 확인을 위한 유니온파인드
			parent=new int[arr.size()];

			//부모를 자기자신으로 세팅
			for(int i=0;i<arr.size();i++) {
				parent[i]=i;
			}

			//크루스칼
			int cnt=0;//선택된 간선의 갯수
			int ans=0;
			for(int i=0;i<arr.size();i++) {
				Node cur=arr.get(i);
				int pa=find(cur.a);
				int pb=find(cur.b);

				if(pa==pb) {
					//만약 같은 유니온이면 사이클 생기니까 넘어가
					continue;
				}

				cnt++;//간선갯수 카운트
				ans+=cur.w;//가중치 더함
				parent[pa]=pb;//유니온 합침

				//mst완성되면 탈출
				if(cnt==r*c-1)
					break;
			}

			pw.println(ans);
		}

		br.close();
		pw.flush();
		pw.close();	
	}
}