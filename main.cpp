#include <fstream>
#include <cmath>
// setprecision
#include <iomanip>

#include <set>
#include <vector>
#include <stack>


bool paint_it_black(const std::vector<std::vector<int>> &graph)
{
    std::vector<int> colors(graph.size(), -1);
    std::stack<int> s{};
    bool flag{true};

    int i{0};
    int color{};
    while (i < graph.size() && flag)
    {
        if (colors[i] == -1)
        {
            s.push(i);
            colors[i] = 1;

            while (!s.empty())
            {
                int vertex = s.top();
                s.pop();
                color = 3 - colors[vertex];
                for (auto neighbour : graph[vertex])
                {
                    if (colors[vertex] == colors[neighbour])
                        flag = false;
                    else if (colors[neighbour] == -1)
                    {
                        s.push(neighbour);
                        colors[neighbour] = color;
                    }
                }
            }
        }
        ++i;
    }
    return flag;
}

std::vector<int> get_colors(const std::vector<std::vector<int>> &graph)
{
    std::vector<int> colors(graph.size(), -1);
    std::stack<int> s{};

    int color{};
    for (int i{0}; i < graph.size(); ++i)
    {
        if (colors[i] == -1)
        {
            s.push(i);
            colors[i] = 1;

            while (!s.empty())
            {
                int vertex = s.top();
                s.pop();
                color = 3 - colors[vertex];
                for (auto neighbour : graph[vertex])
                {
                    if (colors[neighbour] == -1)
                    {
                        s.push(neighbour);
                        colors[neighbour] = color;
                    }
                }
            }
        }
    }
    return colors;
}

std::vector<std::vector<int>> make_graph(int number_of_radio_towers, const std::vector<std::vector<int>> &distances, int radius)
{
    std::vector<std::vector<int>> graph(number_of_radio_towers);
    for (int i{0}; i < number_of_radio_towers; ++i)
    {
        for (int j{0}; j < number_of_radio_towers; ++j)
        {
            if (i != j && distances[i][j] < radius)
                graph[i].push_back(j);
        }
    }
    return graph;
}

int r_bin_search(const std::vector<std::vector<int>> &distances, const std::vector<int> &v, int number_of_radio_towers)
{
    std::size_t l{0};
    std::size_t r{v.size() - 1};
    std::size_t m{};
    while (l < r)
    {
        m = l + (r - l + 1) / 2;
        if (paint_it_black(make_graph(number_of_radio_towers, distances, v[m])))
            l = m;
        else
            r = m - 1;
    }
    return v[l];
}

std::vector<int> set_to_vector(std::set<int> &s)
{
    return std::vector<int>(s.begin(), s.end());
};

int main()
{
    std::ifstream inf{"input.txt"};
    std::ofstream outf("output.txt");

    int number_of_radio_towers{};
    inf >> number_of_radio_towers;

    std::vector<std::vector<int>> radio_towers(number_of_radio_towers);
    int x{};
    int y{};
    for (int i{0}; i < number_of_radio_towers; ++i)
    {
        inf >> x >> y;
        radio_towers[i].push_back(x);
        radio_towers[i].push_back(y);
    }

    std::vector<std::vector<int>> distances(number_of_radio_towers, std::vector<int>(number_of_radio_towers, -1));

    std::set<int> set_of_all_distances{};

    int x1 {};
    int x2{};
    int y1{};
    int y2{};
    int distance{};
    for (int i{0}; i < number_of_radio_towers; ++i)
    {
        for (int j{i + 1}; j < number_of_radio_towers; ++j)
        {
            x1 = radio_towers[i][0];
            y1 = radio_towers[i][1];
            x2 = radio_towers[j][0];
            y2 = radio_towers[j][1];

            distance = std::pow((x2 - x1), 2) + std::pow((y2 - y1), 2);
            distances[i][j] = distance;
            distances[j][i] = distance;
            set_of_all_distances.insert(distance);
        }
    }

    int radius {r_bin_search(distances, set_to_vector(set_of_all_distances), number_of_radio_towers)};
    std::vector<int> colors {get_colors(make_graph(number_of_radio_towers, distances, radius))};
    
    outf << std::setprecision(20) << std::sqrt(radius) / 2 << '\n';

    for (auto element: colors)
        outf << element << ' ';
    outf << std::endl;

    return 0;
}