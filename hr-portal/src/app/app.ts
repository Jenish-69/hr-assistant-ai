import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  imports: [CommonModule, FormsModule],
  templateUrl: './app.html',
  styleUrls: ['./app.css']
})
export class App {

  title = 'HR Portal';
  currentPage = 'dashboard';

  attendanceData: any = {};

  leaveData = {
    employee_id: 101,
    leave_type: '',
    from_date: '',
    to_date: '',
    reason: ''
  };

  leaveMessage = '';

  regularizationData = {
    employee_id: 101,
    date: '',
    entry_time: '',
    exit_time: '',
    reason: '',
    description: ''
  };

  regularizationMessage = '';

  question = '';

  answer = '';

chatMessages: any[] = [
  {
    sender: 'bot',
    text: 'Hi! I am your HR Assistant. Ask me about leave, attendance, or regularization.'
  }
];

  constructor(private http: HttpClient) {}

  changePage(page: string) {
    this.currentPage = page;

    if (page === 'attendance') {
      this.loadAttendance();
    }
  }

  loadAttendance() {
    this.http.get('http://127.0.0.1:8000/attendance')
      .subscribe((data) => {
        this.attendanceData = data;
        console.log(this.attendanceData);
      });
  }

  applyLeave() {
    this.http.post('http://127.0.0.1:8000/apply-leave', this.leaveData)
      .subscribe((response: any) => {
        this.leaveMessage = response.message;
        console.log(response);
      });
  }

  submitRegularization() {
    this.http.post(
      'http://127.0.0.1:8000/regularize',
      this.regularizationData
    )
    .subscribe((response: any) => {
      this.regularizationMessage = response.message;
      console.log(response);
    });
  }

  askAssistant() {
    this.http.post(
      'http://127.0.0.1:8000/ask',
      {
        question: this.question
      }
    )
    .subscribe((response: any) => {
      this.answer = response.answer;
      console.log(response);
    });
  }

}