import { createQueue } from 'kue';

const queue = createQueue();

const data = {
  phoneNumber: '12345678910',
  message: 'You are validated',
}

const queueJob = queue.create('push_notification_code', data).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${queueJob.id}`);
  }
});

queueJob.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', () => {
  console.log('Notification job failed');
});
