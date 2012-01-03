//
//  Timeslot.h
//  Qcumber
//
//  Created by Chris Cooper on 12-01-01.
//  Copyright (c) 2012 __MyCompanyName__. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <CoreData/CoreData.h>


@interface Timeslot : NSManagedObject

@property (nonatomic, strong) NSNumber * day;
@property (nonatomic, strong) NSString * end_time;
@property (nonatomic, strong) NSString * start_time;
@property (nonatomic, strong) NSManagedObject *sectionComponents;

@end
