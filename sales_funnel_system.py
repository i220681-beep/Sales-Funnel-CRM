import os

class Customer:
    """Customer class to store customer information"""
    def __init__(self, customer_id, name, email, phone, potential_value):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.potential_value = potential_value  # Scale of 1-10

    def __str__(self):
        return f"ID: {self.customer_id} | Name: {self.name} | Email: {self.email} | Potential: {self.potential_value}/10"

    def get_display_info(self):
        return f"{self.name} (Value: {self.potential_value}/10)"



class Queue:
    """Queue implementation for managing incoming leads (FIFO)"""
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add item to the back of the queue"""
        self.items.append(item)

    def dequeue(self):
        """Remove and return item from the front of the queue"""
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        """View the item at the front without removing"""
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        """Check if queue is empty"""
        return len(self.items) == 0

    def size(self):
        """Get the number of items in queue"""
        return len(self.items)

    def display(self):
        """Display all items in queue"""
        if self.is_empty():
            return "No leads in queue"
        return "Queue: " + " -> ".join([item.get_display_info() for item in self.items])

class Stack:
    """Stack implementation for managing follow-up tasks (LIFO)"""
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add item to the top of the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return item from the top of the stack"""
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        """View the item at the top without removing"""
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        """Check if stack is empty"""
        return len(self.items) == 0

    def size(self):
        """Get the number of items in stack"""
        return len(self.items)

    def display(self):
        """Display all items in stack"""
        if self.is_empty():
            return "No follow-up tasks"
        return "Follow-ups (top to bottom): " + " | ".join([item.get_display_info() for item in reversed(self.items)])

class SortingAlgorithms:
    """Collection of sorting algorithms for customer lists"""

    @staticmethod
    def bubble_sort(customers, key='potential_value'):
        """Bubble sort implementation"""
        n = len(customers)
        sorted_list = customers.copy()

        for i in range(n):
            for j in range(0, n - i - 1):
                if getattr(sorted_list[j], key) < getattr(sorted_list[j + 1], key):
                    sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
        return sorted_list

    @staticmethod
    def selection_sort(customers, key='potential_value'):
        """Selection sort implementation"""
        sorted_list = customers.copy()
        n = len(sorted_list)

        for i in range(n):
            max_idx = i
            for j in range(i + 1, n):
                if getattr(sorted_list[j], key) > getattr(sorted_list[max_idx], key):
                    max_idx = j
            sorted_list[i], sorted_list[max_idx] = sorted_list[max_idx], sorted_list[i]
        return sorted_list

    @staticmethod
    def insertion_sort(customers, key='potential_value'):
        """Insertion sort implementation"""
        sorted_list = customers.copy()

        for i in range(1, len(sorted_list)):
            key_val = sorted_list[i]
            j = i - 1
            while j >= 0 and getattr(sorted_list[j], key) < getattr(key_val, key):
                sorted_list[j + 1] = sorted_list[j]
                j -= 1
            sorted_list[j + 1] = key_val
        return sorted_list

class SearchingAlgorithms:
    """Collection of searching algorithms for customer lists"""

    @staticmethod
    def linear_search(customers, search_term, search_by='name'):
        """Linear search implementation"""
        results = []
        for customer in customers:
            if search_by == 'name' and search_term.lower() in customer.name.lower():
                results.append(customer)
            elif search_by == 'id' and str(search_term) == str(customer.customer_id):
                results.append(customer)
        return results

    @staticmethod
    def binary_search(customers, search_term, search_by='id'):
        """Binary search implementation (requires sorted list by ID)"""
        # First sort by ID for binary search
        sorted_customers = sorted(customers, key=lambda x: x.customer_id)

        left, right = 0, len(sorted_customers) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_value = str(sorted_customers[mid].customer_id)

            if mid_value == str(search_term):
                return [sorted_customers[mid]]
            elif mid_value < str(search_term):
                left = mid + 1
            else:
                right = mid - 1

        return []

class Sales:
    """Main sales management system"""
    def __init__(self):
        self.lead_queue = Queue()
        self.followup_stack = Stack()
        self.customers = []
        self.customer_counter = 1000

        # Initialize with sample Pakistani customers
        self._initialize_sample_data()

    def _initialize_sample_data(self):
        """Initialize system with sample Pakistani customer data"""
        pakistani_names = [
            ("Ahmed Hassan", "ahmed.hassan@email.com", "0300-1234567", 8),
            ("Fatima Ali", "fatima.ali@email.com", "0301-2345678", 9),
            ("Bilal Khan", "bilal.khan@email.com", "0302-3456789", 7),
            ("Ayesha Siddiqui", "ayesha.siddiqui@email.com", "0303-4567890", 6),
            ("Omar Ahmed", "omar.ahmed@email.com", "0304-5678901", 8),
            ("Zainab Malik", "zainab.malik@email.com", "0305-6789012", 9),
            ("Hassan Raza", "hassan.raza@email.com", "0306-7890123", 7),
            ("Mariam Iqbal", "mariam.iqbal@email.com", "0307-8901234", 8),
            ("Usman Sheikh", "usman.sheikh@email.com", "0308-9012345", 6),
            ("Sanaullah Bhatti", "sanaullah.bhatti@email.com", "0309-0123456", 9),
            ("Rabia Noor", "rabia.noor@email.com", "0310-1234567", 7),
            ("Imran Qureshi", "imran.qureshi@email.com", "0311-2345678", 8),
            ("Nida Khan", "nida.khan@email.com", "0312-3456789", 6),
            ("Tariq Aziz", "tariq.aziz@email.com", "0313-4567890", 9),
            ("Seema Bano", "seema.bano@email.com", "0314-5678901", 7)
        ]

        for name, email, phone, value in pakistani_names:
            self.add_customer(name, email, phone, value)

    def add_customer(self, name, email, phone, potential_value):
        """Add a new customer to the system"""
        customer = Customer(self.customer_counter, name, email, phone, potential_value)
        self.customers.append(customer)
        self.customer_counter += 1
        return customer

    def add_lead(self, name, email, phone, potential_value):
        """Add a new lead to the queue"""
        customer = Customer(self.customer_counter, name, email, phone, potential_value)
        self.lead_queue.enqueue(customer)
        self.customer_counter += 1
        return customer

    def process_lead(self):
        """Process the next lead from the queue"""
        if self.lead_queue.is_empty():
            return None

        customer = self.lead_queue.dequeue()
        self.customers.append(customer)
        return customer

    def add_followup(self, customer_id):
        """Add a follow-up task for a customer"""
        customer = self.find_customer_by_id(customer_id)
        if customer:
            self.followup_stack.push(customer)
            return True
        return False

    def complete_followup(self):
        """Complete the next follow-up task"""
        if self.followup_stack.is_empty():
            return None
        return self.followup_stack.pop()

    def find_customer_by_id(self, customer_id):
        """Find a customer by ID"""
        for customer in self.customers:
            if str(customer.customer_id) == str(customer_id):
                return customer
        return None

    def sort_customers(self, algorithm='bubble'):
        """Sort customers using specified algorithm"""
        if algorithm == 'bubble':
            return SortingAlgorithms.bubble_sort(self.customers)
        elif algorithm == 'selection':
            return SortingAlgorithms.selection_sort(self.customers)
        elif algorithm == 'insertion':
            return SortingAlgorithms.insertion_sort(self.customers)
        else:
            return self.customers

    def search_customers(self, search_term, search_by='name', algorithm='linear'):
        """Search customers using specified algorithm"""
        if algorithm == 'linear':
            return SearchingAlgorithms.linear_search(self.customers, search_term, search_by)
        elif algorithm == 'binary' and search_by == 'id':
            return SearchingAlgorithms.binary_search(self.customers, search_term, search_by)
        else:
            return []

    def get_system_stats(self):
        """Get current system statistics"""
        return {
            'total_customers': len(self.customers),
            'leads_in_queue': self.lead_queue.size(),
            'followup_tasks': self.followup_stack.size(),
            'next_lead': self.lead_queue.peek(),
            'next_followup': self.followup_stack.peek()
        }


class Main:
    """Main application class with menu interface"""
    def __init__(self):
        self.sales_system = Sales()


    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*60)
        print("SALES FUNNEL MANAGEMENT SYSTEM")
        print("="*60)
        print("1. Add New Lead to Queue")
        print("2. Process Next Lead")
        print("3. Add Follow-up Task")
        print("4. Complete Follow-up Task")
        print("5. View All Customers")
        print("6. Sort Customers")
        print("7. Search Customers")
        print("8. View System Status")
        print("9. Exit")
        print("-"*60)
        print("💡 Tip: Menu shows once. After each task, just enter your next choice!")


    def get_user_choice(self, prompt, valid_choices):
        """Get validated user choice"""
        while True:
            try:
                choice = input(prompt).strip()
                if choice in valid_choices:
                    return choice
                print(f"Please enter one of: {', '.join(valid_choices)}")
            except KeyboardInterrupt:
                print("\nExiting...")
                return '9'


    def add_lead_interface(self):
        """Interface for adding a new lead"""
        print("\n--- Add New Lead ---")
        name = input("Enter customer name: ").strip()
        email = input("Enter email: ").strip()
        phone = input("Enter phone: ").strip()

        while True:
            try:
                potential = int(input("Enter potential value (1-10): ").strip())
                if 1 <= potential <= 10:
                    break
                print("Please enter a value between 1 and 10")
            except ValueError:
                print("Please enter a valid number")

        customer = self.sales_system.add_lead(name, email, phone, potential)
        print(f"✓ Lead added successfully! ID: {customer.customer_id}")


    def process_lead_interface(self):
        """Interface for processing the next lead"""
        print("\n--- Process Next Lead ---")
        customer = self.sales_system.process_lead()
        if customer:
            print(f"✓ Lead processed and moved to customer database!")
            print(f"Customer: {customer}")
        else:
            print("⚠ No leads in queue to process")


    def add_followup_interface(self):
        """Interface for adding a follow-up task"""
        print("\n--- Add Follow-up Task ---")
        customer_id = input("Enter customer ID for follow-up: ").strip()

        if self.sales_system.add_followup(customer_id):
            print("✓ Follow-up task added successfully!")
        else:
            print("⚠ Customer not found")


    def complete_followup_interface(self):
        """Interface for completing a follow-up task"""
        print("\n--- Complete Follow-up Task ---")
        customer = self.sales_system.complete_followup()
        if customer:
            print(f"✓ Follow-up completed for: {customer.name}")
        else:
            print("⚠ No follow-up tasks to complete")


    def view_customers_interface(self):
        """Interface for viewing all customers"""
        print("\n--- All Customers ---")
        if not self.sales_system.customers:
            print("No customers in database")
            return

        for i, customer in enumerate(self.sales_system.customers, 1):
            print(f"{i}. {customer}")



    def sort_customers_interface(self):
        """Interface for sorting customers with algorithm selection"""
        print("\n--- Sort Customers ---")
        print("Sort by:")
        print("1. Bubble Sort")
        print("2. Selection Sort")
        print("3. Insertion Sort")

        choice = self.get_user_choice("Choose sorting algorithm (1-3): ", ['1', '2', '3'])

        algorithms = {'1': 'bubble', '2': 'selection', '3': 'insertion'}
        sorted_customers = self.sales_system.sort_customers(algorithms[choice])

        print(f"\n--- Customers Sorted by {algorithms[choice].title()} Sort (High to Low Value) ---")
        for i, customer in enumerate(sorted_customers, 1):
            print(f"{i}. {customer}")



    def search_customers_interface(self):
        """Interface for searching customers with algorithm selection"""
        print("\n--- Search Customers ---")
        print("Search by:")
        print("1. Name (Linear Search)")
        print("2. ID (Linear Search)")
        print("3. ID (Binary Search)")

        choice = self.get_user_choice("Choose search method (1-3): ", ['1', '2', '3'])

        if choice == '1':
            search_term = input("Enter name to search: ").strip()
            results = self.sales_system.search_customers(search_term, 'name', 'linear')
        elif choice == '2':
            search_term = input("Enter ID to search: ").strip()
            results = self.sales_system.search_customers(search_term, 'id', 'linear')
        else:
            search_term = input("Enter ID to search: ").strip()
            results = self.sales_system.search_customers(search_term, 'id', 'binary')

        if results:
            print(f"\n--- Found {len(results)} result(s) ---")
            for customer in results:
                print(customer)
        else:
            print("No customers found matching your search")


    def view_status_interface(self):
        """Interface for viewing system status"""
        print("\n--- System Status ---")
        stats = self.sales_system.get_system_stats()

        print(f"Total Customers: {stats['total_customers']}")
        print(f"Leads in Queue: {stats['leads_in_queue']}")
        print(f"Follow-up Tasks: {stats['followup_tasks']}")

        if stats['next_lead']:
            print(f"Next Lead: {stats['next_lead'].get_display_info()}")
        else:
            print("Next Lead: None")

        if stats['next_followup']:
            print(f"Next Follow-up: {stats['next_followup'].get_display_info()}")
        else:
            print("Next Follow-up: None")

        print(f"\nQueue Status: {self.sales_system.lead_queue.display()}")
        print(f"Follow-up Status: {self.sales_system.followup_stack.display()}")



    def run(self):
        """Main application loop"""
        print("Welcome to Sales Funnel Management System!")
        print("This system demonstrates Queue, Stack, Sorting, and Searching data structures")
        print("=" * 60)

        # Display menu once at startup
        self.display_menu()

        while True:
            try:
                print("\n" + "-" * 30)
                choice = self.get_user_choice("Enter your choice (1-9): ", ['1', '2', '3', '4', '5', '6', '7', '8', '9'])
                print("-" * 30)

                if choice == '1':
                    self.add_lead_interface()
                elif choice == '2':
                    self.process_lead_interface()
                elif choice == '3':
                    self.add_followup_interface()
                elif choice == '4':
                    self.complete_followup_interface()
                elif choice == '5':
                    self.view_customers_interface()
                elif choice == '6':
                    self.sort_customers_interface()
                elif choice == '7':
                    self.search_customers_interface()
                elif choice == '8':
                    self.view_status_interface()
                elif choice == '9':
                    print("\nThank you for using Sales Funnel Management System!")
                    break

                # Simple prompt for next action instead of redisplaying menu
                print("\n✓ Task completed!")

            except KeyboardInterrupt:
                print("\n\nThank you for using Sales Funnel Management System!")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                print("\n⚠️  Please try again!")


if __name__ == "__main__":
    app = Main()
    app.run()